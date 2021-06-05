package org.woxjavafx.dialogs;

import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;

public class InformationAlert {

  public static void showEnchantmentInformation() {
    Alert alert = new Alert(AlertType.INFORMATION);
    alert.setTitle("Info");
    alert.setHeaderText("Enchantment Information");
    alert.setContentText(
        "* Material enchantments on accessories have no effect\n"
            + "* Elemental damage only effect weapons\n"
            + "* Elemental resistance only effect armor/accessories\n\n"
            + "The stats displayed already takes these into account");
    alert.showAndWait();
  }

  public static void showSpecialWeaponPowersInformation() {
    Alert alert = new Alert(AlertType.INFORMATION);
    alert.setTitle("Info");
    alert.setHeaderText("Special Weapon Powers");
    alert.setContentText(
        "Weapons can have these special powers that affect damage:\n"
            + "\tBeast Bopper   - 3x damage against Beasts\n"
            + "\tBug Zapper     - 3x damage against Insects\n"
            + "\tDragon Slayer  - 3x damage against Dragons\n"
            + "\tGolem Smasher  - 3x damage against Golems\n"
            + "\tMonster Masher - 3x damage against Monsters\n"
            + "\tUndead Eater   - 3x damage against Undead");
    alert.showAndWait();
  }

  public static void showAboutInfo() {
    Alert alert = new Alert(AlertType.INFORMATION);
    alert.setTitle("About");
    alert.setHeaderText("World of Xeen equipment information");
    alert.setContentText("Copyleft© 2021");
    alert.showAndWait();
  }
}
