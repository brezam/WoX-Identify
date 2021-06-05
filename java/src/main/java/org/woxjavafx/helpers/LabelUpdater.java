package org.woxjavafx.helpers;

import javafx.scene.control.Label;
import org.woxjavafx.helpers.enums.ElementalBonusType;
import org.woxjavafx.models.dto.Attribute;
import org.woxjavafx.models.dto.Bonus;
import org.woxjavafx.models.dto.Equip;
import org.woxjavafx.models.dto.Material;
import org.woxjavafx.models.dto.Weapon;

public class LabelUpdater {

  public static void updateLabelForBoth(
      Label label, Bonus bonus, Attribute attribute, Material material) {
    StringBuilder newLabelText = new StringBuilder();
    if (material != null) {
      newLabelText.append(getSignedInteger(material.getToHit())).append("\n");
      newLabelText.append(getPhysicalDamage(material.getDamage()));
    } else {
      newLabelText.append("-\n-\n");
    }
    appendElementalBonustoBuilder(newLabelText, attribute, ElementalBonusType.BOTH);
    newLabelText.append(material != null ? getSignedInteger(material.getAc()) : "-").append("\n");
    newLabelText.append(bonus != null ? bonus.getBonus() : "-");
    label.setText(newLabelText.toString());
  }

  public static void updateLabelForEquip(
      Label label, Bonus bonus, Attribute attribute, Material material, Equip equip) {
    StringBuilder newLabelText = new StringBuilder();
    newLabelText.append("-\n-\n");
    appendElementalBonustoBuilder(newLabelText, attribute, ElementalBonusType.EQUIP);
    String ac;
    if (equip.getAc() == 0) {
      ac = "-";
    } else {
      ac = getSignedInteger(equip.getAc() + (material != null ? material.getAc() : 0));
    }
    newLabelText.append(ac).append("\n");
    newLabelText.append(bonus != null ? bonus.getBonus() : "-");
    label.setText(newLabelText.toString());
  }

  public static void updateLabelForWeapon(
      Label label, Bonus bonus, Attribute attribute, Material material, Weapon weapon) {
    StringBuilder newLabelText = new StringBuilder();
    int materialDamage;
    if (material != null) {
      newLabelText.append(getSignedInteger(material.getToHit())).append("\n");
      materialDamage = material.getDamage();
    } else {
      newLabelText.append("-\n");
      materialDamage = 0;
    }
    newLabelText.append(getPhysicalDamage(materialDamage, weapon));
    appendElementalBonustoBuilder(newLabelText, attribute, ElementalBonusType.WEAPON);
    newLabelText.append("-\n");
    newLabelText.append(bonus != null ? bonus.getBonus() : "-").append("\n");
    label.setText(newLabelText.toString());
  }

  private static String getSignedInteger(int integer) {
    return (integer < 0 ? "-" : "+") + integer;
  }

  private static String getPhysicalDamage(int materialDamage) {
    return String.format("%s%n", getSignedInteger(materialDamage));
  }

  private static String getPhysicalDamage(int materialDamage, Weapon weapon) {
    return String.format(
        "%d → %d (%s %s)%n",
        materialDamage + weapon.getDamageRange()[0],
        materialDamage + weapon.getDamageRange()[1],
        weapon.getDamage(),
        getSignedInteger(materialDamage));
  }

  private static void appendElementalBonustoBuilder(
      StringBuilder builder, Attribute attribute, ElementalBonusType displayType) {
    if (attribute == null) {
      builder.append("-\n-\n");
    } else if (displayType == ElementalBonusType.BOTH) {
      builder
          .append(attribute.getElement())
          .append(" ")
          .append(attribute.getElemDam())
          .append("\n");
      builder
          .append(attribute.getElement())
          .append(" ")
          .append(attribute.getElemRes())
          .append("\n");
    } else if (displayType == ElementalBonusType.WEAPON) {
      builder
          .append(attribute.getElement())
          .append(" ")
          .append(attribute.getElemDam())
          .append("\n-\n");
    } else {
      builder
          .append("-\n")
          .append(attribute.getElement())
          .append(" ")
          .append(attribute.getElemRes())
          .append("\n");
    }
  }
}
