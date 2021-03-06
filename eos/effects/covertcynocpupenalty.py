# Used by:
# Subsystem: Legion Offensive - Assault Optimization
# Subsystem: Legion Offensive - Drone Synthesis Projector
# Subsystem: Legion Offensive - Liquid Crystal Magnifiers
# Subsystem: Loki Offensive - Hardpoint Efficiency Configuration
# Subsystem: Loki Offensive - Projectile Scoping Array
# Subsystem: Loki Offensive - Turret Concurrence Registry
# Subsystem: Proteus Offensive - Dissonic Encoding Platform
# Subsystem: Proteus Offensive - Drone Synthesis Projector
# Subsystem: Proteus Offensive - Hybrid Propulsion Armature
# Subsystem: Tengu Offensive - Accelerated Ejection Bay
# Subsystem: Tengu Offensive - Magnetic Infusion Basin
# Subsystem: Tengu Offensive - Rifling Launcher Pattern
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemIncrease(lambda mod: mod.item.requiresSkill("Cynosural Field Theory"),
                                     "covertCloakCPUAdd", module.getModifiedItemAttr("covertCloakCPUPenalty"))

