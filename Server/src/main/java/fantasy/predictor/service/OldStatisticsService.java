package fantasy.predictor.service;

import java.util.List;

import fantasy.predictor.entity.enums.Position;
import fantasy.predictor.entity.old.OldDefense;
import fantasy.predictor.entity.old.OldKicker;
import fantasy.predictor.entity.old.OldOffense;

public interface OldStatisticsService {
  List<OldOffense> getOldOffenseByPosition(Position position);
  List<OldOffense> getOldOffense();

  List<OldKicker> getOldKickers();

  List<OldDefense> getOldDefense();
}
