def compare_ini_settings(content1, content2):
    import configparser
    from io import StringIO

    config1 = configparser.ConfigParser(strict=False)
    config1.read_file(StringIO(content1))

    config2 = configparser.ConfigParser(strict=False)
    config2.read_file(StringIO(content2))

    settings1 = {section: dict(config1.items(section)) for section in config1.sections()}
    settings2 = {section: dict(config2.items(section)) for section in config2.sections()}

    changed_settings = {}
    added_settings = {}
    removed_settings = {}

    for section in settings1.keys() & settings2.keys():
        changed = {key: (settings1[section][key], settings2[section][key]) for key in settings1[section] if key in settings2[section] and settings1[section][key] != settings2[section][key]}
        if changed:
            changed_settings[section] = changed

    for section in settings2.keys() - settings1.keys():
        added_settings[section] = settings2[section]

    for section in settings1.keys() - settings2.keys():
        removed_settings[section] = settings1[section]

    return changed_settings, added_settings, removed_settings

def display_changes(changed_settings, added_settings, removed_settings):
    if changed_settings:
        print("\nChanged Settings:")
        for key, (old_val, new_val) in changed_settings.items():
            print(f"{key}: {old_val} → {new_val}")

    if added_settings:
        print("\nAdded Settings:")
        for key, value in added_settings.items():
            print(f"{key} = {value}")

    if removed_settings:
        print("\nRemoved Settings:")
        for key, value in removed_settings.items():
            print(f"{key} = {value}")

    if not (changed_settings or added_settings or removed_settings):
        print("No differences found between the files.")

# Usage example
# file1 = r'C:\Program Files\Epic Games\UE_5.4\Templates\TP_VirtualRealityBP\Config\DefaultEngine.ini'
# file2 = r'C:\Users\vvox\Documents\UnrealProjects\TheBasement-main\Config\DefaultEngine.ini'

# changed_settings, added_settings, removed_settings = compare_ini_settings(file1, file2)
# display_changes(changed_settings, added_settings, removed_settings)