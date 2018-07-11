package fantasy.predictor.service;

import java.util.List;

import fantasy.predictor.entity.enums.Position;
import fantasy.predictor.entity.enums.Site;
import fantasy.predictor.entity.predictions.DefensePrediction;
import fantasy.predictor.entity.predictions.KickerPrediction;
import fantasy.predictor.entity.predictions.OffensePrediction;

public interface PredictionService {
  List<OffensePrediction> getOffensePrediction();

  List<OffensePrediction> getOffensePredictionByPosition(Position position);

  List<OffensePrediction> getOffensePredictionBySite(Site site);

  List<KickerPrediction> getKickerPrediction();

  List<OffensePrediction> getOffensePredictionByPositionAndSite(Position position, Site site);

  List<KickerPrediction> getKickerPredictionBySite(Site site);

  List<DefensePrediction> getDefensePrediction();

  List<DefensePrediction> getDefensePredictionBySite(Site site);
}
