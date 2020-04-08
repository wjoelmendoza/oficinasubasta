-- MySQL Script generated by MySQL Workbench
-- mar 31 mar 2020 19:23:09
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema oficina_subasta
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema oficina_subasta
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `oficina_subasta` DEFAULT CHARACTER SET utf8 ;
USE `oficina_subasta` ;

-- -----------------------------------------------------
-- Table `oficina_subasta`.`ROL`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ROL` (
  `id_rol` INT UNSIGNED NOT NULL,
  `descripcion` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id_rol`),
  UNIQUE INDEX `id_rol_UNIQUE` (`id_rol` ASC)
)ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `oficina_subasta`.`USUARIO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `USUARIO` (
  `id_cliente` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombres` VARCHAR(250) NOT NULL,
  `fecha_vencimiento` DATE NULL,
  `clave` VARCHAR(20) NOT NULL,
  `id_rol` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id_cliente`),
  INDEX `fk_USUARIO_ROL1_idx` (`id_rol` ASC),
  CONSTRAINT `fk_USUARIO_ROL1`
    FOREIGN KEY (`id_rol`)
    REFERENCES `ROL` (`id_rol`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `oficina_subasta`.`TIPO_DOCUMENTO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `oficina_subasta`.`TIPO_DOCUMENTO` (
  `id_tipo_doc` INT NOT NULL,
  `descripcion` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id_tipo_doc`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `oficina_subasta`.`MEMBRESIA`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `oficina_subasta`.`MEMBRESIA` (
  `id_membresia` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `fecha_pago` DATE NOT NULL,
  `fecha_vencimiento` DATE NOT NULL,
  `id_tipo_doc` INT NOT NULL,
  `id_cliente` INT UNSIGNED NOT NULL,
  `monto` DOUBLE NOT NULL,
  PRIMARY KEY (`id_membresia`),
  INDEX `fk_MEMBRESIA_CLIENTE_idx` (`id_cliente` ASC),
  INDEX `fk_MEMBRESIA_TIPO_DOCUMENTO1_idx` (`id_tipo_doc` ASC),
  CONSTRAINT `fk_MEMBRESIA_CLIENTE`
    FOREIGN KEY (`id_cliente`)
    REFERENCES `oficina_subasta`.`USUARIO` (`id_cliente`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_MEMBRESIA_TIPO_DOCUMENTO1`
    FOREIGN KEY (`id_tipo_doc`)
    REFERENCES `oficina_subasta`.`TIPO_DOCUMENTO` (`id_tipo_doc`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

INSERT INTO ROL values (1, "CLIENTE"), (2, "EMPLEADO");
INSERT INTO TIPO_DOCUMENTO values(1,"BOLETA_BANCO"),(2,"RECIBO");

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


