package org.woxjavafx.models.dto;

import java.util.Objects;

public class Bonus {

  private String name;

  private String bonus;

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public String getBonus() {
    return bonus;
  }

  public void setBonus(String bonus) {
    this.bonus = bonus;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;
    Bonus bonus = (Bonus) o;
    return Objects.equals(name, bonus.name);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name);
  }

  @Override
  public String toString() {
    return "Bonus{" + "name='" + name + '\'' + ", bonus='" + bonus + '\'' + '}';
  }
}
