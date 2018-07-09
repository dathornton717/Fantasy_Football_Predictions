package fantasy.predictor.entity.enums;

// Represents an NFL team
public enum Team {
  ARI("ARI"), ATL("ATL"), BAL("BAL"), BUF("BUF"), CAR("CAR"), CHI("CHI"), CIN("CIN"), CLE("CLE"),
  DAL("DAL"), DEN("DEN"), DET("DET"), GB("GB"), HOU("HOU"), IND("IND"), JAX("JAX"), KC("KC"),
  LAC("LAC"), LAR("LAR"), MIA("MIA"), MIN("MIN"), NE("NE"), NO("NO"), NYG("NYG"), NYJ("NYJ"),
  OAK("OAK"), PHI("PHI"), PIT("PIT"), SEA("SEA"), SF("SF"), TB("TB"), TEN("TEN"), WAS("WAS");

  private String value;

  Team(String value) {
    this.value = value;
  }

  /**
   * Get the String value of the NFL team.
   * @return The String value of the the NFL team
   */
  public String getValue() {
    return value;
  }

  /**
   * Parse the given String into a team or null if the String is not a valid team.
   * @param s The String to parse
   * @return The team or null if the String is not a valid team
   */
  public static Team parse(String s) {
    for (Team team : Team.values()) {
      if (team.getValue().equals(s)) {
        return team;
      }
    }
    return null;
  }
}
