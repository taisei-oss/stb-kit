# Changelog

STB-KITの利用者に影響する重要な変更を記録します。

STB-KITのバージョンについての考え方は[COMPATIBILITY](COMPATIBILITY.md)に従います。

## [Unreleased]

### Breaking

- なし

### Added

- なし

### Changed

- なし

### Deprecated

- なし

### Removed

- なし

### Fixed

- IFC,PLY変換で壁・スラブの板厚が不明の際の既定値10mmに対し、mへの単位変換が二重にされてしまい、0.01mmになっていた問題を修正

### Security

- なし

## [0.1.0b1]

### Added

- CLIのsummaryコマンドを公開
- CLIのupgradeコマンドを公開

### Changed

- 開発ステータスをアルファ版からベータ版へ変更

### Fixed

- ST-Bridge v2.0.0が読み込めない問題を修正
- ST-Bridge v2.0.0からv2.0.2以降へ更新できない問題を修正
- stbkit.api.__all__の誤記を修正
- 空のXML要素で最小回数が1以上である要素が書き出し時に削除される問題を修正

## [0.1.0a9]

### Added

- ST-Bridgeを扱う基本APIを公開
- ST-Bridgeのバリデーション機能を公開
- ST-BridgeからPLY・IFCへの変換機能を公開
- XML差分比較機能を公開
- CLIの基本機能を公開

Copyright 2026 TAISEI CORPORATION
