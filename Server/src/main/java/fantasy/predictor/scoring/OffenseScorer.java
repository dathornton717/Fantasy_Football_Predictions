package fantasy.predictor.scoring;

import fantasy.predictor.entity.old.OldOffense;

public class OffenseScorer {
  private static final double PASS_YARDS = 1.0 / 25.0;
  private static final double PASS_TDS = 4.0;
  private static final double INTERCEPTIONS = -2.0;
  private static final double RUSH_YARDS = 1.0 / 10.0;
  private static final double RUSH_TDS = 6.0;
  private static final double RECEIVING_YARDS = 1.0 / 10.0;
  private static final double RECEIVING_TDS = 6.0;
  private static final double TWO_POINT = 2.0;
  private static final double FUMBLES_LOST = -2.0;
  private static final double FUMBLE_TDS = 6.0;

  public static double totalPoints(OldOffense o) {
    return PASS_YARDS * o.getPassYards()
            + PASS_TDS * o.getPassTd()
            + INTERCEPTIONS * o.getInterceptions()
            + RUSH_YARDS * o.getRushYards()
            + RUSH_TDS * o.getRushTd()
            + RECEIVING_YARDS * o.getRecYards()
            + RECEIVING_TDS * o.getRecTd()
            + TWO_POINT * o.getTwoPt()
            + FUMBLES_LOST * o.getFumLost()
            + FUMBLE_TDS * o.getFumTd();
  }
}
