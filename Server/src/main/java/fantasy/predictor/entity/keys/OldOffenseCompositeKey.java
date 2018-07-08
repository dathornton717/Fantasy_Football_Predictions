package fantasy.predictor.entity.keys;

import java.io.Serializable;

import fantasy.predictor.entity.enums.Position;
import fantasy.predictor.entity.enums.Team;

public class OldOffenseCompositeKey implements Serializable {
  private String name;
  private String team;
  private String position;
}
