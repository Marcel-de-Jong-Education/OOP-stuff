from create_character import CreateCharacter

char0 = CreateCharacter("test", "wizard", 200)
char1 = CreateCharacter("test0", "warrior", 12)

print(
    "Names:\n",
    char0.get_name(), char1.get_name(),
    "\nClasstypes:\n",
    char0.get_classtype(), char1.get_classtype(),
    "\nLevels:\n",
    char0.get_level(), char1.get_level()
)

char0.set_name("marireo")
char0.set_classtype("chump")
char0.set_level(4)
char1.set_name("lemmy")
char1.set_classtype("mage")
char1.set_level(500)

print(
    "Names:\n",
    char0.get_name(), char1.get_name(),
    "\nClasstypes:\n",
    char0.get_classtype(), char1.get_classtype(),
    "\nLevels:\n",
    char0.get_level(), char1.get_level()
)

