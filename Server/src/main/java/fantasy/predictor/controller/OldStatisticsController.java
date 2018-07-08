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

@RestController
public class OldStatisticsController {
  private final OldStatisticsService oldStatisticsService;

  @Autowired
  public OldStatisticsController(OldStatisticsService oldStatisticsService) {
    this.oldStatisticsService = oldStatisticsService;
  }

  @RequestMapping(value = "/api/oldStats/{position}", method = RequestMethod.GET)
  public List<OldOffense> getOldOffenseByPosition(@PathVariable String position) {
    if (Position.parse(position) == null) {
      return new ArrayList<OldOffense>();
    }

    return oldStatisticsService.getOldOffenseByPosition(Position.parse(position));
  }

  @RequestMapping(value = "/api/oldStats/allOffense", method = RequestMethod.GET)
  public List<OldOffense> getOldOffense() {
    return oldStatisticsService.getOldOffense();
  }

  @RequestMapping(value = "/api/oldStats/kicker", method = RequestMethod.GET)
  public List<OldKicker> getOldKickers() {
    return oldStatisticsService.getOldKickers();
  }

  @RequestMapping(value = "/api/oldStats/defense", method = RequestMethod.GET)
  public List<OldDefense> getOldDefense() {
    return oldStatisticsService.getOldDefense();
  }
}
