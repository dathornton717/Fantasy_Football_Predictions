package fantasy.predictor.entity.keys;

import java.io.Serializable;
import java.util.Objects;

public class OldKickerCompositeKey implements Serializable {
  private String name;
  private String team;

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

  @Override
  public int hashCode() {
    return Objects.hash(name, team);
  }
}
