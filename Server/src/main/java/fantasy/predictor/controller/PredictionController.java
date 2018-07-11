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

// Class to control prediction stats for the upcoming season
@RestController
public class PredictionController {
  private final PredictionService predictionService;

  @Autowired
  PredictionController(PredictionService predictionService) {
    this.predictionService = predictionService;
  }

  /**
   * Get all offense predictions for all sites and offensive positions.
   * @return A list of offense predictions
   */
  @RequestMapping(value="/api/prediction/offense", method = RequestMethod.GET)
  public List<OffensePrediction> getOffensePrediction() {
    return predictionService.getOffensePrediction();
  }

  /**
   * Get offense predictions for all sites for the given position.
   * @param position The position to get predictions for
   * @return A list of offense predictions of the given position
   */
  @RequestMapping(value = "/api/prediction/offense/{position}", method = RequestMethod.GET)
  public List<OffensePrediction> getOffensePredictionByPosition(@PathVariable String position) {
    if (Position.parse(position) == null) {
      return new ArrayList<OffensePrediction>();
    }

    return predictionService.getOffensePredictionByPosition(Position.parse(position));
  }

  /**
   * Get offense predictions for all positions for the given site.
   * @param site The site to get predictions for
   * @return A list of offense predictions of the given site
   */
  @RequestMapping(value = "/api/prediction/offense/{site}", method = RequestMethod.GET)
  public List<OffensePrediction> getOffensePredictionBySite(@PathVariable String site) {
    if (Site.parse(site) == null) {
      return new ArrayList<OffensePrediction>();
    }

    return predictionService.getOffensePredictionBySite(Site.parse(site));
  }

  /**
   * Get offense predictions for the given position and site.
   * @param position The position to get predictions for
   * @param site The site to get predictions for
   * @return A list of offense predictions of the given position and site
   */
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

  /**
   * Get predictions for all sites for all kickers.
   * @return A list of kicker predictions for all sites
   */
  @RequestMapping(value = "/api/prediction/kicker", method = RequestMethod.GET)
  public List<KickerPrediction> getKickerPrediction() {
    return predictionService.getKickerPrediction();
  }

  /**
   * Get predictions for kickers for the given site.
   * @param site The site to get predictions from
   * @return A list of kicker predictions for the given site
   */
  @RequestMapping(value = "/api/prediction/kicker/{site}", method = RequestMethod.GET)
  public List<KickerPrediction> getKickerPredictionBySite(@PathVariable String site) {
    if (Site.parse(site) == null) {
      return new ArrayList<KickerPrediction>();
    }

    return predictionService.getKickerPredictionBySite(Site.parse(site));
  }

  /**
   * Get predictions for defenses for all sites.
   * @return A list of defense predictions for all sites
   */
  @RequestMapping(value = "/api/prediction/defense", method = RequestMethod.GET)
  public List<DefensePrediction> getDefensePrediction() {
    return predictionService.getDefensePrediction();
  }

  /**
   * Get predictions for defenses for the given site.
   * @param site The site to get predictions from
   * @return A list of defense predictions for the given site
   */
  @RequestMapping(value = "/api/prediction/defense/{site}", method = RequestMethod.GET)
  public List<DefensePrediction> getDefensePredictionBySite(@PathVariable String site) {
    if (Site.parse(site) == null) {
      return new ArrayList<DefensePrediction>();
    }

    return predictionService.getDefensePredictionBySite(Site.parse(site));
  }
}
