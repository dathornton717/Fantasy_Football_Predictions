package fantasy.predictor.entity.keys;

import java.io.Serializable;
import java.util.Objects;

public class KickerPredictionCompositeKey implements Serializable {
  private String name;
  private String team;
  private String site;

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }

    if (!(o instanceof KickerPredictionCompositeKey)) {
      return false;
    }

    KickerPredictionCompositeKey that = (KickerPredictionCompositeKey) o;
    return name.equals(that.name) && team.equals(that.team) && site.equals(that.site);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, team, site);
  }
}
