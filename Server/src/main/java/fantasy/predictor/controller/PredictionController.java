package fantasy.predictor.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

import fantasy.predictor.entity.enums.Position;
import fantasy.predictor.entity.enums.Site;
import fantasy.predictor.entity.predictions.DefensePrediction;
import fantasy.predictor.entity.predictions.KickerPrediction;
import fantasy.predictor.entity.predictions.OffensePrediction;
import fantasy.predictor.service.PredictionService;

@RestController
public class PredictionController {
  private final PredictionService predictionService;

  @Autowired
  PredictionController(PredictionService predictionService) {
    this.predictionService = predictionService;
  }

  @RequestMapping(value="/api/prediction/offense", method = RequestMethod.GET)
  public List<OffensePrediction> getOffensePrediction() {
    return predictionService.getOffensePrediction();
  }

  @RequestMapping(value = "/api/prediction/offense/{position}", method = RequestMethod.GET)
  public List<OffensePrediction> getOffensePredictionByPosition(@PathVariable String position) {
    if (Position.parse(position) == null) {
      return new ArrayList<OffensePrediction>();
    }

    return predictionService.getOffensePredictionByPosition(Position.parse(position));
  }

  @RequestMapping(value = "/api/prediction/offense/{site}", method = RequestMethod.GET)
  public List<OffensePrediction> getOffensePredictionBySite(@PathVariable String site) {
    if (Site.parse(site) == null) {
      return new ArrayList<OffensePrediction>();
    }

    return predictionService.getOffensePredictionBySite(Site.parse(site));
  }

  @RequestMapping(value = "/api/prediction/offense/{position}/{site}", method = RequestMethod.GET)
  public List<OffensePrediction> getOffensePredictionByPositionAndSite(
          @PathVariable String position,
          @PathVariable String site) {
    if (Position.parse(position) == null) {
      return new ArrayList<OffensePrediction>();
    }

    if (Site.parse(site) == null) {
      return new ArrayList<OffensePrediction>();
    }

    return predictionService
            .getOffensePredictionByPositionAndSite(Position.parse(position), Site.parse(site));
  }

  @RequestMapping(value = "/api/prediction/kicker", method = RequestMethod.GET)
  public List<KickerPrediction> getKickerPrediction() {
    return predictionService.getKickerPrediction();
  }

  @RequestMapping(value = "/api/prediction/kicker/{site}", method = RequestMethod.GET)
  public List<KickerPrediction> getKickerPredictionBySite(@PathVariable String site) {
    if (Site.parse(site) == null) {
      return new ArrayList<KickerPrediction>();
    }

    return predictionService.getKickerPredictionBySite(Site.parse(site));
  }

  @RequestMapping(value = "/api/prediction/defense", method = RequestMethod.GET)
  public List<DefensePrediction> getDefensePrediction() {
    return predictionService.getDefensePrediction();
  }

  @RequestMapping(value = "/api/prediction/defense/{site}", method = RequestMethod.GET)
  public List<DefensePrediction> getDefensePredictionBySite(@PathVariable String site) {
    if (Site.parse(site) == null) {
      return new ArrayList<DefensePrediction>();
    }

    return predictionService.getDefensePredictionBySite(Site.parse(site));
  }


}
