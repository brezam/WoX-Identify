package org.woxjavafx.controller;

import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.stream.Stream;
import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import org.woxjavafx.dialogs.InformationAlert;
import org.woxjavafx.helpers.DataLoader;
import org.woxjavafx.helpers.LabelUpdater;
import org.woxjavafx.models.dto.Attribute;
import org.woxjavafx.models.dto.Bonus;
import org.woxjavafx.models.dto.Equip;
import org.woxjavafx.models.dto.Material;
import org.woxjavafx.models.dto.Weapon;

public class PrimaryController {

  private static final Map<String, Bonus> bonusesMap = DataLoader.getBonusesMap();
  private static final Map<String, Weapon> weaponsMap = DataLoader.getWeaponsMap();
  private static final Map<String, Material> materialsMap = DataLoader.getMaterialsMap();
  private static final Map<String, Equip> equipMap = DataLoader.getEquipMap();
  private static final Map<String, Attribute> attributesMap = DataLoader.getAttributesMap();

  private final Bonus[] bonus = new Bonus[2];
  private final Weapon[] weapon = new Weapon[2];
  private final Material[] material = new Material[2];
  private final Equip[] equip = new Equip[2];
  private final Attribute[] attribute = new Attribute[2];

  @FXML private List<TextField> attFields;
  @FXML private List<TextField> nameFields;
  @FXML private List<Circle> attCircles;
  @FXML private List<Circle> nameCircles;
  @FXML private List<Label> statsLabels;

  @FXML
  public void onMenuFileExitAction() {
    Platform.exit();
  }

  @FXML
  public void showEnchantmentInformation() {
    InformationAlert.showEnchantmentInformation();
  }

  @FXML
  public void showSpecialWeaponPowersInformation() {
    InformationAlert.showSpecialWeaponPowersInformation();
  }

  @FXML
  public void showAboutInfo() {
    InformationAlert.showAboutInfo();
  }

  @FXML
  public void onField0Action() {
    updateObjects(0);
  }

  @FXML
  public void onField1Action() {
    updateObjects(1);
  }

  private void updateObjects(int side) {
    String att = attFields.get(side).getText().trim();
    bonus[side] = bonusesMap.get(att);
    if (bonus[side] != null) {
      attribute[side] = null;
      material[side] = null;
    } else {
      attribute[side] = attributesMap.get(att);
      if (attribute[side] != null) {
        material[side] = null;
      } else {
        material[side] = materialsMap.get(att);
      }
    }
    String name = nameFields.get(side).getText().trim();
    weapon[side] = weaponsMap.get(name);
    equip[side] = equipMap.get(name);
    update(side);
  }

  private void update(int side) {
    if (Stream.of(bonus[side], attribute[side], material[side]).allMatch(Objects::isNull)) {
      attCircles.get(side).setFill(Color.DARKRED);
    } else {
      attCircles.get(side).setFill(Color.GREEN);
    }
    if (weapon[side] == null && equip[side] == null) {
      nameCircles.get(side).setFill(Color.DARKRED);
      LabelUpdater.updateLabelForBoth(
          statsLabels.get(side), bonus[side], attribute[side], material[side]);
    } else if (weapon[side] == null) {
      nameCircles.get(side).setFill(Color.GREEN);
      LabelUpdater.updateLabelForEquip(
          statsLabels.get(side), bonus[side], attribute[side], material[side], equip[side]);
    } else {
      nameCircles.get(side).setFill(Color.GREEN);
      LabelUpdater.updateLabelForWeapon(
          statsLabels.get(side), bonus[side], attribute[side], material[side], weapon[side]);
    }
  }
}
