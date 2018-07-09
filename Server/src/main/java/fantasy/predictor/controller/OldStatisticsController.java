package fantasy.predictor.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

import fantasy.predictor.entity.old.OldDefense;
import fantasy.predictor.entity.old.OldKicker;
import fantasy.predictor.entity.old.OldOffense;
import fantasy.predictor.entity.enums.Position;
import fantasy.predictor.service.OldStatisticsService;

// Class to control old stats from the previous year
@RestController
public class OldStatisticsController {
  private final OldStatisticsService oldStatisticsService;

  @Autowired
  public OldStatisticsController(OldStatisticsService oldStatisticsService) {
    this.oldStatisticsService = oldStatisticsService;
  }

  /**
   * Get a list of players given the position.
   * @param position The position of players to look up
   * @return The list of players and their stats
   */
  @RequestMapping(value = "/api/oldStats/{position}", method = RequestMethod.GET)
  public List<OldOffense> getOldOffenseByPosition(@PathVariable String position) {
    if (Position.parse(position) == null) {
      return new ArrayList<OldOffense>();
    }

    return oldStatisticsService.getOldOffenseByPosition(Position.parse(position));
  }

  /**
   * Get all offensive positions stats.
   * @return A list of all offensive players containing their stats
   */
  @RequestMapping(value = "/api/oldStats/allOffense", method = RequestMethod.GET)
  public List<OldOffense> getOldOffense() {
    return oldStatisticsService.getOldOffense();
  }

  /**
   * Get kicker stats from last year.
   * @return A list of kickers from last year and their stats
   */
  @RequestMapping(value = "/api/oldStats/kicker", method = RequestMethod.GET)
  public List<OldKicker> getOldKickers() {
    return oldStatisticsService.getOldKickers();
  }

  /**
   * Get defense stats from last year.
   * @return A list of defenses from last year and their stats
   */
  @RequestMapping(value = "/api/oldStats/defense", method = RequestMethod.GET)
  public List<OldDefense> getOldDefense() {
    return oldStatisticsService.getOldDefense();
  }
}
