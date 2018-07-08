package fantasy.predictor.entity;

import java.io.Serializable;

import fantasy.predictor.entity.enums.Position;
import fantasy.predictor.entity.enums.Team;

public class OffenseCompositeKey implements Serializable {
  private String name;
  private String team;
  private String position;
}
