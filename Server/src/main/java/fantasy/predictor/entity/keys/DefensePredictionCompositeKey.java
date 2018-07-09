package fantasy.predictor.entity.keys;

import java.io.Serializable;
import java.util.Objects;

public class DefensePredictionCompositeKey implements Serializable {
  private String name;
  private String site;

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

  @Override
  public int hashCode() {
    return Objects.hash(name, site);
  }
}
