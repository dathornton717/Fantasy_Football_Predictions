package fantasy.predictor.entity.keys;

import java.io.Serializable;
import java.util.Objects;

// Represents a composite key in the database for a defense prediction
public class DefensePredictionCompositeKey implements Serializable {
  private String name;
  private String site;

  /**
   * Does this DefensePredictionCompositeKey equal the given Object?
   * @param o The given object
   * @return If the objects have the same name and site.
   */
  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }

    if (!(o instanceof DefensePredictionCompositeKey)) {
      return false;
    }

    DefensePredictionCompositeKey that = (DefensePredictionCompositeKey) o;
    return name.equals(that.name) && site.equals(that.site);
  }

  /**
   * Generates a hash of this DefensePredictionCompositeKey.
   * @return The int hash of this DefensePredictionCompositeKey
   */
  @Override
  public int hashCode() {
    return Objects.hash(name, site);
  }
}
