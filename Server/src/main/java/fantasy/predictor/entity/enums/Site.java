package fantasy.predictor.entity.enums;

// Represents a site that predicts fantasy points
public enum Site {
  NFL("NFL.com"), CBS("cbssports.com"), ESPN("ESPN.com");

  private String value;

  Site(String value) {
    this.value = value;
  }

  /**
   * Get the String value of the site.
   * @return The value of the site
   */
  public String getValue() {
    return value;
  }

  /**
   * Parse the given String into a site or return null if it is not a valid String.
   * @param s The String to check
   * @return The site or null if illegal
   */
  public static Site parse(String s) {
    for (Site site : Site.values()) {
      if (site.getValue().equals(s)) {
        return site;
      }
    }
    return null;
  }
}
