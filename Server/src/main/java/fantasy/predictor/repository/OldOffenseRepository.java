package fantasy.predictor.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

import fantasy.predictor.entity.keys.OldOffenseCompositeKey;
import fantasy.predictor.entity.old.OldOffense;

public interface OldOffenseRepository extends JpaRepository<OldOffense, OldOffenseCompositeKey> {

  List<OldOffense> findByPosition(String position);
}
