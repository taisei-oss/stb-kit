# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from ..common import ElementHook
from .hook_funcs.hook_common import hook_apply_conditions_list
from .hook_funcs.hook_joint_beam_shape_h import joint_beam_shape_h
from .hook_funcs.hook_sec_pile_rc import sec_pile_rc
from .hook_funcs.hook_sec_pile_s import sec_pile_s
from .hook_funcs.hook_sec_slab_deck import sec_slab_deck
from .hook_funcs.hook_sec_slab_rc import sec_slab_rc

HOOKS: dict[str, ElementHook] = {
    "StbApplyConditionsList": hook_apply_conditions_list,
    "StbSecPile_RC": sec_pile_rc,
    "StbSecPile_S": sec_pile_s,
    "StbSecSlab_RC": sec_slab_rc,
    "StbJointBeamShapeH": joint_beam_shape_h,
    "StbSecSlabDeck": sec_slab_deck,
}
