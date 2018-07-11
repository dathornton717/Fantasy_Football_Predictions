package fantasy.predictor.entity.enums;

public enum Site {
  NFL("NFL.com"), CBS("cbssports.com"), ESPN("ESPN.com");

  private String value;

  Site(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  public static Site parse(String s) {
    for (Site site : Site.values()) {
      if (site.getValue().equals(s)) {
        return site;
      }
    }
    return null;
  }
}
