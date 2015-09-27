from __future__ import unicode_literals
from django.contrib import admin

from .models import *

admin.site.register(Ability)
admin.site.register(AbilityName)
admin.site.register(AbilityDescription)
admin.site.register(AbilityFlavorText)
admin.site.register(AbilityChange)
admin.site.register(AbilityChangeDescription)

admin.site.register(Berry)
admin.site.register(BerryFirmness)
admin.site.register(BerryFirmnessName)
admin.site.register(BerryFlavor)

admin.site.register(Characteristic)
admin.site.register(CharacteristicDescription)

admin.site.register(ContestCombo)
admin.site.register(ContestEffectDescription)
admin.site.register(ContestEffect)
admin.site.register(ContestType)
admin.site.register(ContestTypeName)

admin.site.register(EggGroup)
admin.site.register(EggGroupName)

admin.site.register(EncounterCondition)
admin.site.register(EncounterConditionValue)
admin.site.register(EncounterConditionName)
admin.site.register(EncounterConditionValueName)
admin.site.register(EncounterConditionValueMap)
admin.site.register(EncounterMethod)
admin.site.register(EncounterMethodName)
admin.site.register(EncounterSlot)
admin.site.register(Encounter)

admin.site.register(EvolutionChain)
admin.site.register(EvolutionTrigger)
admin.site.register(EvolutionTriggerName)

admin.site.register(Experience)

admin.site.register(Gender)

admin.site.register(Generation)
admin.site.register(GenerationName)

admin.site.register(GrowthRate)
admin.site.register(GrowthRateDescription)

admin.site.register(ItemCategory)
admin.site.register(ItemCategoryName)
admin.site.register(ItemFlag)
admin.site.register(ItemFlagMap)
admin.site.register(ItemFlagDescription)
admin.site.register(ItemFlavorText)
admin.site.register(ItemFlingEffect)
admin.site.register(ItemFlingEffectDescription)
admin.site.register(ItemGameIndex)
admin.site.register(ItemName)
admin.site.register(ItemPocketName)
admin.site.register(ItemPocket)
admin.site.register(ItemDescription)
admin.site.register(Item)

admin.site.register(Language)
admin.site.register(LanguageName)

admin.site.register(LocationAreaEncounterRate)
admin.site.register(LocationAreaName)
admin.site.register(LocationArea)
admin.site.register(LocationGameIndex)
admin.site.register(LocationName)
admin.site.register(Location)

admin.site.register(Machine)

admin.site.register(MoveBattleStyle)
admin.site.register(MoveBattleStyleName)
admin.site.register(MoveChange)
admin.site.register(MoveDamageClass)
admin.site.register(MoveDamageClassDescription)
admin.site.register(MoveEffectChange)
admin.site.register(MoveEffectChangeDescription)
admin.site.register(MoveEffectDescription)
admin.site.register(MoveEffect)
admin.site.register(MoveFlagMap)
admin.site.register(MoveFlagDescription)
admin.site.register(MoveFlag)
admin.site.register(MoveFlavorText)
admin.site.register(MoveLearnMethod)
admin.site.register(MoveLearnMethodName)
admin.site.register(MoveMeta)
admin.site.register(MoveMetaAilment)
admin.site.register(MoveMetaAilmentName)
admin.site.register(MoveMetaCategoryDescription)
admin.site.register(MoveMetaCategory)
admin.site.register(MoveMetaStatChange)
admin.site.register(MoveName)
admin.site.register(MoveTargetDescription)
admin.site.register(MoveTarget)
admin.site.register(Move)

admin.site.register(NatureBattleStylePreference)
admin.site.register(NatureName)
admin.site.register(NaturePokeathlonStat)
admin.site.register(Nature)

admin.site.register(PalParkArea)
admin.site.register(PalParkAreaName)
admin.site.register(PalPark)

admin.site.register(PokeathlonStatName)
admin.site.register(PokeathlonStat)

admin.site.register(Pokedex)
admin.site.register(PokedexVersionGroup)
admin.site.register(PokedexDescription)

admin.site.register(Pokemon)
admin.site.register(PokemonAbility)
admin.site.register(PokemonColor)
admin.site.register(PokemonColorName)
admin.site.register(PokemonDexNumber)
admin.site.register(PokemonEggGroup)
admin.site.register(PokemonEvolution)
admin.site.register(PokemonForm)
admin.site.register(PokemonFormName)
admin.site.register(PokemonFormGeneration)
admin.site.register(PokemonGameIndex)
admin.site.register(PokemonHabitat)
admin.site.register(PokemonHabitatName)
admin.site.register(PokemonItem)
admin.site.register(PokemonMove)
admin.site.register(PokemonShape)
admin.site.register(PokemonShapeName)
admin.site.register(PokemonSpecies)
admin.site.register(PokemonSpeciesName)
admin.site.register(PokemonSpeciesDescription)
admin.site.register(PokemonSpeciesFlavorText)
admin.site.register(PokemonStat)
admin.site.register(PokemonType)

admin.site.register(Region)
admin.site.register(RegionName)

admin.site.register(StatName)
admin.site.register(Stat)

admin.site.register(SuperContestEffect)
admin.site.register(SuperContestCombo)
admin.site.register(SuperContestEffectDescription)

admin.site.register(Type)
admin.site.register(TypeName)
admin.site.register(TypeGameIndex)
admin.site.register(TypeEfficacy)

admin.site.register(Version)
admin.site.register(VersionName)
admin.site.register(VersionGroup)
admin.site.register(VersionGroupMoveLearnMethod)
admin.site.register(VersionGroupRegion)
