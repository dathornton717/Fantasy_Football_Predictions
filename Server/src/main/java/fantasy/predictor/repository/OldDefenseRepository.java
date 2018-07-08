package fantasy.predictor.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import fantasy.predictor.entity.OffenseCompositeKey;
import fantasy.predictor.entity.old.OldDefense;

public interface OldDefenseRepository extends JpaRepository<OldDefense, OffenseCompositeKey> {
}
