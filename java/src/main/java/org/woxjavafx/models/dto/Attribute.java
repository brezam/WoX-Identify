package org.woxjavafx.models.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.Objects;

public class Attribute {

  private String name;

  private String element;

  @JsonProperty("elem_res")
  private String elemRes;

  @JsonProperty("elem_dam")
  private String elemDam;

  private Integer ac;

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public String getElement() {
    return element;
  }

  public void setElement(String element) {
    this.element = element;
  }

  public String getElemRes() {
    return elemRes;
  }

  public void setElemRes(String elemRes) {
    this.elemRes = elemRes;
  }

  public String getElemDam() {
    return elemDam;
  }

  public void setElemDam(String elemDam) {
    this.elemDam = elemDam;
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
    Attribute attribute = (Attribute) o;
    return Objects.equals(name, attribute.name);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name);
  }

  @Override
  public String toString() {
    return "Attribute{"
        + "name='"
        + name
        + '\''
        + ", element='"
        + element
        + '\''
        + ", elemRes='"
        + elemRes
        + '\''
        + ", elemDam='"
        + elemDam
        + '\''
        + ", ac='"
        + ac
        + '\''
        + '}';
  }
}
