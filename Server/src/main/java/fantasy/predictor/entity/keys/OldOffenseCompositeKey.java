package fantasy.predictor.entity.keys;

import java.io.Serializable;
import java.util.Objects;

// Represents a database key for an old offense stat
public class OldOffenseCompositeKey implements Serializable {
  private String name;
  private String team;
  private String position;

  /**
   * Does the given Object equal this OldOffenseCompositeKey?
   * @param o The Object to compare to
   * @return If the given Object has the same name, team, and position as this
   *        OldOffenseCompositeKey
   */
  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }

    if (!(o instanceof OldOffenseCompositeKey)) {
      return false;
    }

    OldOffenseCompositeKey that = (OldOffenseCompositeKey) o;
    return name.equals(that.name) && team.equals(that.team) && position.equals(that.position);
  }

  /**
   * Generate a hash value for this OldOffenseCompositeKey.
   * @return The int hash for this OldOffenseCompositeKey
   */
  @Override
  public int hashCode() {
    return Objects.hash(name, team, position);
  }
}
