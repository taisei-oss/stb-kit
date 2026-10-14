// Copyright 2026 TAISEI CORPORATION
// SPDX-License-Identifier: MPL-2.0
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

use crate::data_model::building_geometry::ElementInfo;

#[derive(Debug, Clone, PartialEq, Eq)]
#[cfg_attr(feature = "serde", derive(serde::Serialize, serde::Deserialize))]
pub struct ElementReference {
    pub guid: Option<String>,
    pub xpath: Option<String>,
}

pub type ElementReferenceHandler = Box<dyn FnMut(&ElementReference) + 'static>;

#[derive(Debug, Clone, PartialEq, Eq)]
#[cfg_attr(feature = "serde", derive(serde::Serialize, serde::Deserialize))]
pub struct ElementClickEvent {
    /// BuildingGeometry::elementsの要素インデックス。要素IDとは異なるので注意。
    pub element_index: usize,
    /// BuildingGeometry::elements.kindの値
    pub kind: u32,
    pub guid: Option<String>,
    pub xpath: Option<String>,
    pub name: Option<String>,
    pub source_type: String,
    /// ST-Bridgeの要素ID。
    pub source_id: Option<String>,
}
impl ElementClickEvent {
    pub(crate) fn from_element_info(element_index: usize, info: ElementInfo<'_>) -> Self {
        Self {
            element_index,
            kind: info.kind,
            guid: info.guid.map(|guid| guid.simple().to_string()),
            xpath: info.xpath.map(str::to_owned),
            name: info.name.map(str::to_owned),
            source_type: info.source_type.to_owned(),
            source_id: info.source_id.map(str::to_owned),
        }
    }

    pub fn element_reference(&self) -> ElementReference {
        ElementReference {
            guid: self.guid.clone(),
            xpath: self.xpath.clone(),
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq)]
#[cfg_attr(feature = "serde", derive(serde::Serialize, serde::Deserialize))]
pub struct NodeClickEvent {
    /// BuildingGeometry::nodes内の節点インデックス。節点IDとは異なるので注意。
    pub node_index: usize,
    /// ST-Bridgeの節点ID。
    pub source_id: String,
    pub guid: Option<String>,
    pub xpath: Option<String>,
}

impl NodeClickEvent {
    /// 節点に対応するStbNodeのパネルを開くための参照を作成する。
    pub fn element_reference(&self) -> ElementReference {
        ElementReference {
            guid: self.guid.clone(),
            xpath: self.xpath.clone(),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::data_model::building_geometry::ElementKind;
    use uuid::Uuid;

    #[test]
    fn element_click_event_from_element_info() {
        let guid = Uuid::parse_str("12345678-1234-5678-1234-567812345678").unwrap();
        let kind = ElementKind::Girder.as_u32();
        let info = ElementInfo {
            kind,
            guid: Some(&guid),
            xpath: Some("/StbModel/StbMembers/StbGirders/StbGirder[1]"),
            name: Some("G1"),
            source_type: "StbGirder",
            source_id: Some("1"),
        };

        let event = ElementClickEvent::from_element_info(4, info);

        assert_eq!(event.element_index, 4);
        assert_eq!(event.kind, kind);
        assert_eq!(
            event.guid.as_deref(),
            Some("12345678123456781234567812345678")
        );
        assert_eq!(event.name.as_deref(), Some("G1"));
        assert_eq!(event.source_type, "StbGirder");

        let reference = event.element_reference();
        assert_eq!(reference.guid, event.guid);
        assert_eq!(reference.xpath, event.xpath);
    }
}
