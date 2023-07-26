# Sims 4 Mods & CC Collection

UP TO DATE WITH [PATCH 1.99](https://www.ea.com/en/games/the-sims/the-sims-4/news/update-07-18-2023)

Alt Dowload at [Mega Upload](https://mega.nz/folder/cu4DRKRC#Larg_jJpLK86AepCrQiH0A)

I recommend [Sims4Studio](https://sims4studio.com/thread/1523/downloading-sims-4-studio) (S4S) for editing and [Sims4ModManager](https://gametimedev.de/S4MM/) (S4MM) for maintaining. Don’t forget to delete `localthumbcache.package` when installing new mods Merged files are typically not used in this collection. 

A few CC/Scripts will require expansion content [I own](https://jakethedog104.tumblr.com/about). If you are missing DLC then you may have an occasional missing mesh and some of the scripts might be irrelevant. For any missing CAS mesh it will show up with [question marks](https://answers.ea.com/t5/image/serverpage/image-id/34573i4EF028DD1BF1AA10) and you can [use BetterExceptons to remove the file](https://twitter.com/TwistedMexi/status/1558120769535737858) or S4MM to turn the file off (*.packageOFF is a file turned off by S4MM).

### CC Rules
All CC comes from reputable creators, is maxis-match and mostly complies to poly limits. The idea behind this mod collection is to keep it true to the spirit of the original game but with fixes, and more customization.

---

## Base Game Conversions
Located: `/BCG_Conversions`

These are Maxis files from DLC exported to the base game. They are sorted by expansion code. 

The object name is changed to follow the pattern:
`OBJECT NAME - DLC`

The object description formats the exporter’s credits to match the maxis standard format.

## BuildBuy
Located: `/BuildBuy`, `/BuildBuy_Labeled_1`, `/BuildBuy_Labeled_2`, `/BuildBuy_Ununified`

Files are loosely organized by type, collection and creator. Original filenames are mostly* kept for consistency with the creator and easy replacement in case of updates.

The object name is changed to follow the pattern:
`[CREATOR_CODE] OBJECT NAME, DESCRIPTOR - COLLECTION`
Descriptor refers to things such as: Tall, Short, Medium, Long, Extra-Long, Solid, Patterned, etc

The object description formats the creator's credits to match the maxis standard format. The key words used are Converted (From a previous Sims game), Extracted (From an existing object), Recolored (Mesh not changed, and likely not included), and Created (Original Mesh or Edit).

This makes the object name more readable, and you can easily search by creator, collection or object name - even in the case of collabs and despite the age of the content. 

Those in `/BuildBuy_Ununified` have not yet been organized. Those in `/BuildBuy_Labeled_#` have been labeled and credited consistently. Those in `/BuildBuy` have been confirmed to have the correct color tag as well. Custom Icons are not kept.

## CAS
Located: `/CAS`, `/CAS_UnUnified`, `/Presets`, `/StyledLooks`

Files are loosely organized by collection and creator. Original filenames are kept for consistency with the creator and easy replacement in case of updates. CAS objects are enabled for random, and not limited by gender by default. CAS objects that are “accessories” but on the wrong “part” (eg: accessory tops listed as “gloves”) as well as the few pieces of alpha CC (currently only sailor moon things) are disabled for random. Custom Icons are not kept except for the objects with intentionally miss-matched parts (eg: accessory tops listed as “gloves”).

Those in `/CAS` have been confirmed to have the correct part type, sub type and color tags.

## Gameplay
Located: `/Aspirations`, `/Career`, `/Events`, `/Poses`, `/TraditionHoliday`, `/Traits`

Original filenames are kept for consistency with the creator and easy replacement in case of updates.

## Script Mods
Located: `/Tmex-BetterBuildBuy`, `/TMEX-Settings`, `/Scripts`

Original filenames are kept for consistency with the creator and easy replacement in case of updates. `/Tmex-BetterBuildBuy` and `/TMEX-Settings` should not be directly changed.

### Script Descriptions
#### BugFixes
- `Carl_DineOut_Reloaded` - Fixes assorted Dine Out expansion pack issues - Requires Dine Out
- `lot51_bathe_around_kittens_puppies_bugfix` - Sims can bath around baby animals - For Cats and Dogs
- `dont_prep_food_where_you_angry_poop` - Can set counters to not allow food prep via shift-click
- `dont_wash_dishes_where_you_angry_poop` - Can set sinks to not allow dish washing via shift-click
- `simularity-fix-carobcake` - fixes required ingredients for the sugar free carob cake to not have sugar - For Cottage Living and Spa Day
- `simularity-rumbasimtinyliving` - fixes missing dance interaction - For Jungle Adventure and Tiny Living
- `simularity-clfixes-betterchickentreats` - increases the distance that chickens will look for thrown treats - Requires Cottage Living
- `BosseladyTV_Homework_at_Desk_3.23` - more likely to use a desk for HW
- `ilkavelle_UniversityRejectionLetter` - can be rejected from university
#### UI/Visual Fixes
- `MizoreYukii_CustomWrenchIcon_BlueCC/SwatchIcon` - Sets CC visual to a blue circle/plumbob rather than a wrench
- `More_CAS_Columns` - CAS shows more columns
- `MMautoShorterTeens` - Teens are shorter than adults
- `Zerbu - More Selectable Icons` - More icons available for clubs and holidays
- `simularity-incensetooltips` - Incense has a tooltip detailing which scent does what - For Spa Day
- `simularity-emotions` - emotions use more descriptive names
- `simularity-awardsnotification` - notifies you of the award event - For Get Famous
- `tmex-BetterBuildBuy` - Build/Buy has searchable debug, live edit is more accessible and has expandable UI
- `LittleMsSam_RSM_BG_RoundDiningTableSlots` - new slot in center of large round tables
- `SimMattically_HD_Maps` - World maps are not blurry
- `MM_StarWarsCostumeHider_V5` - hide star wars
- `MMPlanCareerOutfit` - Change work outfit
#### Basic Support & Tuning
- `lot51_core` - Support script for all Lot51 mods
- `XmlInjector` - Support for some carers/events
- `RVSN_NoSnapCurtain_Slot_OVERRIDE` - Curtains will not snap allowing easier alt-placement
- `Tmex-AlwaysTesting` - Sets testingcheats true 
- `Tmex-BetterExceptions` - More robust error reporting, mod conflict checking and CAS identifier
- `Tmex-LifetimeSkills` - skills from childhood lead into adulthood
- `Tmex-NoWeatherBB` - No weather while in build/buy mode
- `simularity-clfixes-fewerupgradeparts` - reduced the number of upgrade parts needed for shed and coop - Requires Cottage Living
- `simularity-clfixes-foxnokill` - foxes won't kill chickens - Requires Cottage Living
- `simularity-clfixes-lessanimalsadness` - sims will not be sad for as long when animals die - Requires Cottage Living
- `simularity-clfixes-moresocialgain` - easier to befriend animals - Requires Cottage Living
- `MizoreYukii_Scarlet_ShowerWoohooTweaks` - shower whoohoo gives hygiene - Requires Discover University
- `sigma1202_No_sad_holiday_moodlet` - Prevents the disappointing holiday moodlet - Requires Seasons
- `LittleMsSam_RSM_BG_AutoDrinkWhenEating` - Sims will grab a drink with their food
- `LittleMsSam_RSM_BG_AutoPutActivityTableCraftsIntoInventory` - After using a craft table the craft will go to the inventory
- `LittleMsSam_RSM_BG_AutoPutPaintingInInventory_ArtSociety_Tasks` - After using an easel the painting will go to the inventory
- `LittleMsSam_RSM_BG_AutoPutPaintingInInventorys` - After using an easel the painting will go to the inventory
- `LittleMsSam_RSM_BG_AutoUsePicnicTableWhenEating` - Picnic tables can be used autonomously
- `LittleMsSam_RSM_BG_PreferLeftovers` - Sims will prefer leftovers if they exist over cooking
- `LittleMsSam_RSM_EP_CD_CallOverWillWakeUpPets` - Pets will wake up if you call for them - Cats and Dogs Required
- `LittleMsSam_RSM_EP_CD_DogsChangeIntoEverydayAfterWalk` - Dogs will change after a walk - Cats and Dogs Required
- `LittleMsSam_RSM_EP_CD_FasterPickUp` - no more speak to pets before picking them up - Cats and Dogs Required
- `LittleMsSam_RSM_EP_CD_NoSpoilingDriedAnimalFood` - dry animal food will not spoil - Cats and Dogs Required
- `LittleMsSam_RSM_BG_SimCallOverHigherDistance` - you can call sims from further away
- `LittleMsSam_RSM_EP_CoL_GiveGiftsMoreProduceOptionsToRabbits` - More Vegies and Fruits can be gifted to rabbits, and other objects can not be - Cottage Living Required
- `LittleMsSam_RSM_EP_CoL_OrderMoreGroceries` - More groceries are available order and certain item limits are increased - Cottage Living Required
- `LittleMsSam_RSM_EP_IL_ToddlerPlayInOceanWithSeashell` - Toddlers playing in the ocean will use a shell not a duck - Island Living Required
- `LittleMsSam_RSM_EP_S_MoreCustomesForWearCostumeHoliday` - more outfits count towards “Wear Costume” tradition - Seasons Required
- `LittleMsSam_RSM_EP_S_NoKidsOutdoorObjectsinRainOrHeavySnow` - kids will not be able to use certain objects if the object it outside and it is raining - Seasons Required
- `LittleMsSam_RSM_EP_S_NoPresentOpeningCooldown` - Presents no longer have a cooldown - Seasons Required
- `LittleMsSam_RSM_EP_S_ProtectiveRaincoats` - Raincoats stop you from getting wet - Seasons Required
- `LittleMsSam_RSM_GP_P_SackLunchInInventory` - After making a sack lunch it goes into your inventory - Parenting Required
- `LittleMsSam_RSM_SP_K_SellMoreKnittingObjectsViaRetail` - more objects can be sold at retail - Knifty Knitting Required
- `LittleMsSam_NoAutoFoodGrabAfterCooking` - Chef won’t autonomously eat
- `LittleMsSam_HiredEmployeesEarnMoney` - employees get paid
- `LittleMsSam_EcoDishwasher` - Dishwasher runs less often
- `LittleMsSam_ChangeOutfitCloset` - Can change outfits on coat racks and with closets
- `Simvasion_knittingautonomy_fix` - Tuning for knitting
- `Arckange_BetterLadders` - Ladders are faster
- `LittleMsSam_SLO` - Laundry is better
- `MizoreYukii_RemoveHatsMoreIndoors` - No hats inside
#### New Interactions
- `Carl_CollectiblesReady` - Shift-Click a Sim to select the “Find Collectables” action which sends the sim on a treasure hunt in their current neighborhood
- `Carl_TrytoMakeFriends` - New friendly interactions “Try to Make Friends”
- `Lumpinou_ReRollWants_Cheat` - Shift-Click a Sim to choose to re-roll wants
- `MTS_Scumbumbo_EvolveAll_BM` - While gardening “Evolve” will be treated like “Water” and effect all applicable plants
- `MTS_Scumbumbo_WorkingMedicineCabinets` - You can buy medicine from medicine cabinets & some mirrors - Requires Get To Work
- `RVSN_PlayComputerChess_OVERRIDE` - Sims can play chess on the computer (replaces BlicBlock)
- `lot51_extinguisher` - Adds cheat code fire.extinguish, or sos
- `LittleMsSam_RSM_BG_ClaimAllTheThings` - Shift-click to claim random objects
- `LittleMsSam_RSM_BG_ReleaseAllTheGhosts` - Ghosts can all be released at once, and urns summoned if someone dies off the lot
- `LittleMsSam_RSM_EP_CD_BuyTreatsViaPC` - treats can be purchased from PC - Cats and Dogs Required
- `LittleMsSam_RSM_EP_SE_HealthyFoodOnFridges` - “Cook Healthy Meal” available to all - Snowy Escape Required
- `LittleMsSam_AdvancedBirthCertificate` - birth certificate if you give birth at a hospital - Get To Work Required
- `LittleMsSam_AutomaticStereoSystem` - stereos can be upgraded to automatically turn off
- `LittleMsSam_CanIComeOver` - can ask a sim from the relationship panel to visit
- `LittleMsSam_GoForAWalkCats` - Cats can go for a walk too - Cats and Dogs Required
- `LittleMsSam_PetFoodOverhaul` - can bulk cook pet meals
- `LittleMsSam_SmallInviteToHangOutOverhaul` - can invite family to hang even if you have not met them
- `LittleMsSam_TrainPuppies` - puppies can be taught basic tricks - Cats and Dogs Required
- `LittleMsSam_TransferInventory` - can transfer your inventory with a single click
- `LittleMsSam_WorkingPetWaterBowls` - water bowls for pets - Cats and Dogs Required
- `Mercuryfoam_Piano_OneClickPerformAllSongs_Mod` -  Can perform all songs at once
#### New Gameplay
- `mc_*` - Overall game control and cheats
- `Lumpinou_LGBTQIA_Mod` - Enables queer identities and stories
- `MTS_Scumbumbo_KeepBooksAfterPublishing_UpdatedByLittleMsSam` - After publishing a book your sim will keep a copy of it in their inventory
- `MTS_Scumbumbo_MoldingClayBuildsCreativity_UpdatedbyLittleMsSam` - Playing with clay allows children to build their creativity skill
- `MTS_Scumbumbo_TraumaticDivorceForChildren_UpdatedbyLittleMsSam` - Divorce has more of an impact on children
- `Scumbumbo_PackingCrates_BMFix` - Packing crates exist so you can move out sims with Build/Buy Items - REMOVED as it is currently broken
- `lot51_simzlink` - Adds the requirement to add internet service to lots to use internet-based interactions
- `lot51_doorbell` - A modern doorbell with improved notifications
- `lot51_plumbbros` - An alternative to the Thermostat/Temperature system
- `lot51_sunrise` - Re-introduces alarm clocks
- `thepancake1-MoreTraitsInCAS` - CAS allows you to set 5 traits instead of 3
- `simularity-preference-reading` - Sims will have preferred reading genres
- `simularity-medications` -This mod contains three medications to help with my mental illness traits
- `LittleMsSam_SulSulWeatherApp` - can check the weather before you travel
- `LittleMsSam_SimDaDatingApp` - Sims have a dating app they can use
- `LittleMsSam_Cookbooks` - Cookbooks for regional recipes
- `LittleMsSam_Abortion` - sims can get an abortion
- `LittleMsSam_Miscarriage` - small chance of miscarriage occurring
- `LittleMsSam_HealthyDrinks` - healthy drinks are available
- `LittleMsSam_LiveInBusiness` - can live in your business
- `Lumpinou_OpenLoveLife` - More relationship options (Polyam, ENM, etc)
- `SpinningPlumbobs_ExpandedMermaids` - More interactions & gameplay for mermaids incl. Children
- `Lumpinou_ScienceBabyTweak_InGameChoicePregOrInstant` - Can choose pregnancy
- `Mercuryfoam_BallroomDanceMod`, `Mercuryfoam_Ballet_Barre`, `Mercuryfoam_TRMA_CapoeiraMod`, `Mercuryfoam_PoleDanceMod` - Can learn new dances
- `Mercuryfoam_Hopscotch` - Kids can play hopscotch
- `Basemental_Alcohol` - Sims can get drunk

---

## Patch Notes
### 0.1 ➔ 0.2
- `MizoreYukii_Scarlet_ShowerWoohooTweaks` added, but disabled
- `sigma1202_No_sad_holiday_moodlet` was added
- `Lumpinou_OpenLoveLife` was added
- NEW script mods from LittleMsSam
- NEW Traditions
- NEW CC from SIXAM, SYB, kumika and jaydub, Mostly for Build/Buy
- Most SIXAM CC and F&H was labeled and moved to BB-Label, SYB content still needs to be labeled
### 0.2 ➔ 0.3
- All SYB content labeled and moved to BB-Label, Identified all objects not yet labeled
- Minor Edits to existing BB object’s tags
- NEW Mermaid objects & Expanded Mermaids CC
- NEW littledica BB CC
- NEW traits from Triplis for Kids, and a depression reward trait
- High Chair Fix removed as EA patched it, and removed Family Reunion event
- A many mods are updated, incl LMS & MCCC, and some are disabled as they will require an update from the latest patch (1.96)
### 0.3 ➔ 0.4
- Added Base Game Conversions
- New content, mostly BB, from ATS4, Mac20, Peacemaker and others.
- New makeup CC
- Updated available mods for the latest patch (1.96)
### 0.4 ➔ 0.5
- Modified file names to only include alphanumeric characters, dashes and underscores. This is done for the speed of Sims loading the files.
- Additional CC; new content from creators, disability cc, Max20, and peacemaker, infant stuff
- Lightly Reorganized CC in BuildBuy folder
- Some ununified CC is now unified and some unlabeled CC now labeled
- A few new scripts/tuning
### 0.5 ➔ 0.6
- Updated scripts to the latest patch (1.98)
- Some Additional CC, Some labeling & sorting
### 0.6 ➔ 0.7
- Updated scripts to the latest patch (1.99)
- Some Additional CC, Some labeling & sorting & price changes
