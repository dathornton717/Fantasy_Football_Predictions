package fantasy.predictor.entity.keys;

import java.io.Serializable;
import java.util.Objects;

// Represents a database composite key for an Offense Prediction
public class OffensePredictionCompositeKey implements Serializable {
  private String name;
  private String team;
  private String position;
  private String site;

  /**
   * Does this OffensePredictionCompositeKey equal the given Object?
   * @param o The Object to compare this OffensePredictionCompositeKey to
   * @return If the given Object has the same name, team, position, and site as this
   *        OffensePredictionCompositeKey
   */
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

  /**
   * Generate a hash value for this OffensePredictionCompositeKey.
   * @return The int hash for this OffensePredictionCompositeKey
   */
  @Override
  public int hashCode() {
    return Objects.hash(name, team, position, site);
  }
}
