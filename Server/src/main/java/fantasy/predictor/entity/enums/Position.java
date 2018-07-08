package fantasy.predictor.entity.enums;

public enum Position {
  QB("QB"), RB("RB"), WR("WR"), TE("TE");

  private String value;

  Position(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  public static Position parse(String s) {
    for (Position position : Position.values()) {
      if (position.getValue().equals(s)) {
        return position;
      }
    }
    return null;
  }
}
