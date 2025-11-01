#!/usr/bin/env python3
"""
Fix for issue #2738: Add by_alias=True to model_dump_json() calls

This script updates the freeze format serialization to properly use field aliases
like "basic blocks" instead of "basic_blocks" as documented in the spec.
"""

# The fix is to change:
#   return freeze.model_dump_json()
# To:
#   return freeze.model_dump_json(by_alias=True)
#
# This needs to be applied to both dumps_static() and dumps_dynamic() functions
# in capa/features/freeze/__init__.py at lines 451 and 560
