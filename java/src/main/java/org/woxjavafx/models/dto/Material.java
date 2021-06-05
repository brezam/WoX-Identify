package org.woxjavafx.models.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.Objects;

public class Material {

  private String name;

  @JsonProperty("to_hit")
  private Integer toHit;

  private Integer damage;

  private Integer ac;

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public Integer getToHit() {
    return toHit;
  }

  public void setToHit(Integer toHit) {
    this.toHit = toHit;
  }

  public Integer getDamage() {
    return damage;
  }

  public void setDamage(Integer damage) {
    this.damage = damage;
  }

  public Integer getAc() {
    return ac;
  }

  public void setAc(Integer ac) {
    this.ac = ac;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;
    Material material = (Material) o;
    return Objects.equals(name, material.name);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name);
  }

  @Override
  public String toString() {
    return "Material{"
        + "name='"
        + name
        + '\''
        + ", toHit="
        + toHit
        + ", damage="
        + damage
        + ", ac="
        + ac
        + '}';
  }
}
