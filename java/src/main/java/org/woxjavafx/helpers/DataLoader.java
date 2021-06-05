package org.woxjavafx.helpers;

import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.IOException;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;
import org.woxjavafx.models.dto.Attribute;
import org.woxjavafx.models.dto.Bonus;
import org.woxjavafx.models.dto.Equip;
import org.woxjavafx.models.dto.Material;
import org.woxjavafx.models.dto.Weapon;

public class DataLoader {

  private static final ObjectMapper objectMapper = new ObjectMapper();
  private static Map<String, Bonus> bonusesMap;
  private static Map<String, Weapon> weaponsMap;
  private static Map<String, Material> materialsMap;
  private static Map<String, Equip> equipMap;
  private static Map<String, Attribute> attributesMap;

  public static void loadData(Path jsonResourcePath) throws IOException {
    List<Bonus> bonuses = getListFromJson(jsonResourcePath, "bonus", Bonus[].class);
    List<Weapon> weapons = getListFromJson(jsonResourcePath, "weapons", Weapon[].class);
    List<Material> materials = getListFromJson(jsonResourcePath, "materials", Material[].class);
    List<Equip> equip = getListFromJson(jsonResourcePath, "equip", Equip[].class);
    List<Attribute> attributes = getListFromJson(jsonResourcePath, "attributes", Attribute[].class);

    bonusesMap =
        bonuses.stream().collect(Collectors.toUnmodifiableMap(Bonus::getName, Function.identity()));
    weaponsMap =
        weapons.stream()
            .collect(Collectors.toUnmodifiableMap(Weapon::getName, Function.identity()));
    materialsMap =
        materials.stream()
            .collect(Collectors.toUnmodifiableMap(Material::getName, Function.identity()));
    equipMap =
        equip.stream().collect(Collectors.toUnmodifiableMap(Equip::getName, Function.identity()));
    attributesMap =
        attributes.stream()
            .collect(Collectors.toUnmodifiableMap(Attribute::getName, Function.identity()));
  }

  public static <T> List<T> getListFromJson(
      Path jsonResourcePath, String fileName, Class<T[]> target) throws IOException {
    return Arrays.asList(
        objectMapper.readValue(
            DataLoader.class.getResourceAsStream(jsonResourcePath.resolve(fileName) + ".json"),
            target));
  }

  public static ObjectMapper getObjectMapper() {
    return objectMapper;
  }

  public static Map<String, Bonus> getBonusesMap() {
    return bonusesMap;
  }

  public static Map<String, Weapon> getWeaponsMap() {
    return weaponsMap;
  }

  public static Map<String, Material> getMaterialsMap() {
    return materialsMap;
  }

  public static Map<String, Equip> getEquipMap() {
    return equipMap;
  }

  public static Map<String, Attribute> getAttributesMap() {
    return attributesMap;
  }
}
