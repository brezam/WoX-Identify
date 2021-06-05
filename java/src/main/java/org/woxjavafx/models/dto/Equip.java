package org.woxjavafx.models.dto;

import java.util.Objects;

public class Equip {

  private String name;

  private Integer ac;

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
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
    Equip equip = (Equip) o;
    return Objects.equals(name, equip.name);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name);
  }

  @Override
  public String toString() {
    return "Equip{" + "name='" + name + '\'' + ", ac='" + ac + '\'' + '}';
  }
}
