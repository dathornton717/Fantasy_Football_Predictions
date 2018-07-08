package fantasy.predictor.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import fantasy.predictor.entity.OffenseCompositeKey;
import fantasy.predictor.entity.old.OldKicker;

public interface OldKickerRepository  extends JpaRepository<OldKicker, OffenseCompositeKey> {
}
