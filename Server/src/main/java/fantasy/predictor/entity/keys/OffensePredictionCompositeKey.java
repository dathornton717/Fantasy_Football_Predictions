package fantasy.predictor.entity.keys;

import java.io.Serializable;
import java.util.Objects;

public class OffensePredictionCompositeKey implements Serializable {
  private String name;
  private String team;
  private String position;
  private String site;

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }

    if (!(o instanceof OffensePredictionCompositeKey)) {
      return false;
    }

    OffensePredictionCompositeKey that = (OffensePredictionCompositeKey) o;
    return name.equals(that.name) && team.equals(that.team) && position.equals(that.position)
            && site.equals(that.site);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, team, position, site);
  }
}
