# ST-BridgeからIFCへの変換仕様

このページは、STB-KITのST-BridgeからIFCへの変換仕様を整理したものです。

## 変換のフロー

ST-BridgeからIFCの変換処理は最新版のST-Bridgeからの変換のみ実装しています。

そのため、最新版ではないST-Bridgeを変換する際は、まず、ST-Bridgeを最新版へ変換する処理を行ってからIFCに変換します。

## 空間の対応

ST-Bridgeから生成した部材は、次の空間へ配置します。

- IfcProject
- IfcSite (name="Site")
- IfcBuilding (name="Building")
- IfcBuildingStorey (name="1FL")
- 各部材エンティティ

IfcProject.nameはStbCommonのproject_nameとします。

現在ST-Bridgeの階の設定にかかわらず、すべての要素が1FLに配置されます。
階ごとの配置は今後対応予定です。

## 変換の原則

現在のIFC変換の用途は他分野BIMとの整合確認、干渉チェック等を想定しています。そのため、現状は外形変換のみの実装となっています（細かい属性や配筋情報は変換しない）。

基本的にはST-Bridgeの1つの要素はIFCの1つのエンティティに対応させ、ST-BridgeのguidとIFCのGlobalIdを対応させます。
これにより、IFCの対応するST-Bridge要素やその属性を参照しやすくします。

## ST-Bridge要素とIFCエンティティの対応

部材種別の対応は次のとおりです。

| ST-Bridge部材 | IFCクラス |
| --- | --- |
| StbColumn, StbPost, StbFoundationColumn | IfcColumn |
| StbGirder, StbBeam, StbStripFooting, StbParapet | IfcBeam | 
| StbBrace | IfcMember | 
| StbWall | IfcWall | 
| StbSlab | IfcSlab |
| StbFooting | IfcFooting |
| StbPile | IfcPile |

StbOpenArrangementは現状では独立したIFC部材にはせず、StbWallまたはStbSlabに対応するIfcWall, IfcSlabに形状のみ反映しています。

SRC,CFTについては、親をIfcElementAssemblyとし、子部材をIfcRelAggregatesで関連付けます。
そのため、guidの対応はIfcColumnなどではなく、IfcElementAssemblyが対応します。
guidは一意である必要があることから、IfcColumnなどの子部材のGlobalIdは新規生成します。

下記要素は変換非対応のため、IFCのエンティティが作られません。
- StbIsolatingDevice
- StbDampingDevice 
- StbFrameDampingDevice
- StbPenetrationArrangement
- StbJointArrangement
- StbPanelZoneArrangement
- StbConnectionArrangement

## 幾何表現の対応

### 線材（柱・梁・ブレース・杭・基礎など）

- 断面が単一かつ始端終端で同形状、回転指定なし: 押し出し形状(SweptSolid)
- 断面切替や形状変化あり: 押し出しで表現できないためメッシュ表現(Tessellation)
- 断面がうまく取得できなかった場合: 10mm角の仮断面で表現

ストレート部材以外はメッシュ表現になるため、IFC上で断面がわかりにくい問題があります。
今後、多断面部材もIfcElementAssemblyにする案があります（検討中）。

#### 押し出し時のプロファイル選択

押し出し時は、断面形状の型に応じて次のIFCプロファイルを選びます。

| 断面形状 | IFCプロファイル |
| --- | --- |
| StbSecRoll-BOX | IfcRectangleHollowProfileDef |
| StbSecBuild-BOX （t1 == t2） | IfcRectangleHollowProfileDef |
| StbSecRoll-C  | IfcUShapeProfileDef |
| StbSecColumnCircle,StbSecPile_RC_ConventionalStraight,StbSecFigurePile_RC_Certified, StbSecRoundBar, CFT柱のコンクリート部 | IfcCircleProfileDef |
| StbSecRoll-H, StbSecBuild-H   | IfcIShapeProfileDef |
| StbSecPile_S_Straight, StbSecPipe | IfcCircleHollowProfileDef |
| StbSecColumnRect, StbSecBeamStraight,StbSecFoundation_RC_Rect,StbSecParapet_RC_TypeI, StbSecFlatBar, 鋼管CFT柱のコンクリート部 | IfcRectangleProfileDef |
| StbSecRoll-T, StbSecBuild-T | IfcTShapeProfileDef |
| StbSecLipC  | IfcCShapeProfileDef |


対応していない断面
- StbSecBuild-HAsymmetric
- StbSecRoll-2C
- StbSecRoll-2L
- StbSecLip2C
- StbSecParapet_RC_TypeL
- StbSecParapet_RC_TypeT
- StbSecPilePrecast_PHC 
- StbSecPilePrecast_ST 
- StbSecPilePrecast_SC 
- StbSecPilePrecast_PRC 
- StbSecPilePrecast_CPRC 
- StbSecPilePrecastNodular_PHC 
- StbSecPilePrecastNodular_PRC 
- StbSecPilePrecastNodular_CPRC 
- StbSecPilePrecastProduct
- StbSecSteelProduct

次の場合は、専用ProfileDefを使わず、任意形状(Arbitrary)を使います。
山形鋼はIFCにプロファイルがありますが、ST-Bridgeと配置基準の向きが異なるため、部材座標軸が反対になり、わかりにくくなるため、任意ポリラインで書き出しています。

- ShapeBuildBoxでt1 != t2
- StbSecRoll-L
- その他対応未掲載の断面形状

StbSecUndefined, StbSecSteelUndefinedおよび断面が不明な場合は10×10mmの仮定断面とし、IfcRectangleProfileDefで押し出します。

※現状では鉄骨梁の鉄骨レベルが一律-150になっています。今後修正予定です。

### 面材系部材（壁・スラブ）

- 板材は板厚方向への押し出し形状(SweptSolid)とします
- profileは任意形状(Arbitrary)を利用します
- 開口形状はprofileに含めます。
- 現状では開口の回転には対応していません

#### 板厚の設定

- StbSecSlab_RC_ConventionalStraight, StbSecWall_RC_Straightは通常の板厚を取得します
- テーパー形状は対応していないため、10mmの仮定板厚になります。
- StbSecSlabPrecast, StbSecProductSlabPrecastはST-Bridgeから板厚を取得できないため、10mmの仮定板厚になります。

## 多段面で断面切り替え位置が取得できなかった場合

ST-Bridgeで、断面の切り替え位置の数と断面数がうまく取得できずに整合しなかった場合、警告を出したうえで断面切り替え位置を部材長を等分割した位置に置き換えます。

## GlobalIdの設定方法

- ST-Bridge側の要素にguidがあれば、対応するIFCエンティティのGlobalIdに設定します
- guidがなければ新規guidを生成します
- IfcRelAggregatesやIfcRelContainedInSpatialStructureも新規guidとなります
- SRCとCFTはIfcElementAssemblyに要素のguidが振られるため、子要素のIfcColumn等は新規guidとなります。

## 単位

出力するIFCファイルの長さ単位はmmです。

ST-Bridgeの単位はmmであり、IfcOpenShellへ値を渡す際は、
APIの要求に応じて内部的にmへ変換してから渡していますが、
ファイルの出力単位はmmとなります。

## その他注意事項
- 柱、間柱の基準点はST-Bridge仕様では「図心」となっていますが、現状では「断面の外形を包絡する長方形の中心」として出力しています。
長方形、円形など一般的な断面では問題になりませんが、T形鋼、溝形鋼、山形鋼などの図心位置がずれる断面については注意が必要です。
今後断面の図心計算を検討します。
- 折れ曲がりを表現する中間節点等については非対応です。
- 鉄骨のrの表現は対応していない場合があります。


## エラー時の扱い

- 変換中に問題が生じた場合は、内容に応じて警告やエラーを出力し、可能な限り変換を継続します
- 長さが0部材はエンティティの作成をスキップします
- 断面形状や板厚が不明の時は既定値で代替して警告出力します

Copyright 2026 TAISEI CORPORATION
