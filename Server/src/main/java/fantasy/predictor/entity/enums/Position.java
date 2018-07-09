package fantasy.predictor.entity.enums;

// Represents a different offensive position
public enum Position {
  QB("QB"), RB("RB"), WR("WR"), TE("TE");

  private String value;

  Position(String value) {
    this.value = value;
  }

  /**
   * Get the value of the position.
   * @return The position in String format
   */
  public String getValue() {
    return value;
  }

  /**
   * Parse the given String into a position or return null if it is not a valid position.
   * @param s The String to parse
   * @return The position or null if it is not a valid position
   */
  public static Position parse(String s) {
    for (Position position : Position.values()) {
      if (position.getValue().equals(s)) {
        return position;
      }
    }
    return null;
  }
}
