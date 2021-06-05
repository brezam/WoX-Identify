package org.woxjavafx.models.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.Arrays;
import java.util.Objects;

public class Weapon {

  private String name;

  private String damage;

  @JsonProperty("damagerange")
  private Integer[] damageRange;

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public String getDamage() {
    return damage;
  }

  public void setDamage(String damage) {
    this.damage = damage;
  }

  public Integer[] getDamageRange() {
    return damageRange;
  }

  public void setDamageRange(Integer[] damageRange) {
    this.damageRange = damageRange;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;
    Weapon weapon = (Weapon) o;
    return Objects.equals(name, weapon.name);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name);
  }

  @Override
  public String toString() {
    return "Weapon{"
        + "name='"
        + name
        + '\''
        + ", damage='"
        + damage
        + '\''
        + ", damageRange="
        + Arrays.toString(damageRange)
        + '}';
  }
}
