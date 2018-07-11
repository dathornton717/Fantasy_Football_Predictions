package fantasy.predictor.entity.keys;

import java.io.Serializable;
import java.util.Objects;

// Represents a database composite key for kicker predictions
public class KickerPredictionCompositeKey implements Serializable {
  private String name;
  private String team;
  private String site;

  /**
   * Does this KickerPredictionCompositeKey equal the given Object?
   * @param o The Object to compare this KickerPredictionCompositeKey to
   * @return If the given Object is equal to this KickerPredictionCompositeKey (has the same
   *        name, team, and site)
   */
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

  /**
   * Generate a hash for this KickerPredictionCompositeKey.
   * @return The int hash for this KickerPredictionCompositeKey
   */
  @Override
  public int hashCode() {
    return Objects.hash(name, team, site);
  }
}
