from base import _ropen_j
CALL_JSON_PATH = None

class _patch:
    def __set_rule(self, _dict=_ropen_j(CALL_PATH)):
        rule_ob = {
                "_patch_stable" : _dict["patch_stable"],
                "_patch_beta"   : _dict["patch_beta"],
                "_base"         : _dict["base"],
                "_rule"         : _dict["rule"]
        }
        return rule_ob

    def _call_m(rule=__set_rule()):
        pass
