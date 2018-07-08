package fantasy.predictor.entity.enums;

public enum Team {
  ARI("ARI"), ATL("ATL"), BAL("BAL"), BUF("BUF"), CAR("CAR"), CHI("CHI"), CIN("CIN"), CLE("CLE"),
  DAL("DAL"), DEN("DEN"), DET("DET"), GB("GB"), HOU("HOU"), IND("IND"), JAX("JAX"), KC("KC"),
  LAC("LAC"), LAR("LAR"), MIA("MIA"), MIN("MIN"), NE("NE"), NO("NO"), NYG("NYG"), NYJ("NYJ"),
  OAK("OAK"), PHI("PHI"), PIT("PIT"), SEA("SEA"), SF("SF"), TB("TB"), TEN("TEN"), WAS("WAS");

  private String value;

  Team(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  public static Team parse(String s) {
    for (Team team : Team.values()) {
      if (team.getValue().equals(s)) {
        return team;
      }
    }
    return null;
  }
}
