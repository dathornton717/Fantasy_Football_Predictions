package fantasy.predictor.entity.keys;

import java.io.Serializable;
import java.util.Objects;

// Represents a database key for an old kicker
public class OldKickerCompositeKey implements Serializable {
  private String name;
  private String team;

  /**
   * Does this OldKickerCompositeKey equal the given Object?
   * @param o The Object to compare to
   * @return If the given Object has the same name and team as this OldKickerCompositeKey
   */
  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }

    if (!(o instanceof OldKickerCompositeKey)) {
      return false;
    }

    OldKickerCompositeKey that = (OldKickerCompositeKey) o;
    return name.equals(that.name) && team.equals(that.team);
  }

  /**
   * Generate a hash value for this OldKickerCompositeKey
   * @return The int hash for this OldKickerCompositeKey
   */
  @Override
  public int hashCode() {
    return Objects.hash(name, team);
  }
}
