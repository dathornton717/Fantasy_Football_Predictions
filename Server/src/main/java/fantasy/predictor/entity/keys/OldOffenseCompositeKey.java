package fantasy.predictor.entity.keys;

import java.io.Serializable;
import java.util.Objects;

public class OldOffenseCompositeKey implements Serializable {
  private String name;
  private String team;
  private String position;

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

  @Override
  public int hashCode() {
    return Objects.hash(name, team, position);
  }
}
