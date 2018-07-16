package fantasy.predictor.service.impl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Collections;
import java.util.List;

import fantasy.predictor.entity.enums.Position;
import fantasy.predictor.entity.old.OldDefense;
import fantasy.predictor.entity.old.OldKicker;
import fantasy.predictor.entity.old.OldOffense;
import fantasy.predictor.repository.OldDefenseRepository;
import fantasy.predictor.repository.OldKickerRepository;
import fantasy.predictor.repository.OldOffenseRepository;
import fantasy.predictor.service.OldStatisticsService;

@Service
public class OldStatisticsServiceImpl implements OldStatisticsService {
  private final OldOffenseRepository oldOffenseRepository;
  private final OldKickerRepository oldKickerRepository;
  private final OldDefenseRepository oldDefenseRepository;

  @Autowired
  public OldStatisticsServiceImpl(OldOffenseRepository oldOffenseRepository,
                                  OldKickerRepository oldKickerRepository,
                                  OldDefenseRepository oldDefenseRepository) {
    this.oldOffenseRepository = oldOffenseRepository;
    this.oldKickerRepository = oldKickerRepository;
    this.oldDefenseRepository = oldDefenseRepository;
  }

  @Override
  public List<OldOffense> getOldOffenseByPosition(Position position) {
    return oldOffenseRepository.findByPosition(position.getValue());
  }

  @Override
  public List<OldOffense> getOldOffense() {
    List<OldOffense> result = oldOffenseRepository.findAll();
    Collections.sort(result, Collections.reverseOrder());
    return result;
  }

  @Override
  public List<OldKicker> getOldKickers() {
    return oldKickerRepository.findAll();
  }

  @Override
  public List<OldDefense> getOldDefense() {
    return oldDefenseRepository.findAll();
  }
}
