DROP SCHEMA IF EXISTS `AbuelApp`;
CREATE SCHEMA IF NOT EXISTS `AbuelApp`;
USE `AbuelApp`;

CREATE TABLE `abuelo`
(
    `usuario`   varchar(255) NOT NULL,
    `contra`    BINARY(60)   NOT NULL,
    `nombre`    varchar(255) NOT NULL,
    `apellido`  varchar(255) NOT NULL,
    `celular`   varchar(255) NOT NULL,
    `direccion` varchar(255) NOT NULL,
    `sexo`      varchar(255) DEFAULT NULL,
    `ayudante`  varchar(255) NULL,
    PRIMARY KEY (`usuario`)
);

CREATE TABLE `voluntario`
(
    `usuario`        varchar(255) NOT NULL,
    `contra`         BINARY(60)   NOT NULL,
    `nombre`         varchar(255) NOT NULL,
    `apellido`       varchar(255) NOT NULL,
    `celular`        varchar(255) NOT NULL,
    `direccion`      varchar(255) NOT NULL,
    `sexo`           varchar(255)          DEFAULT NULL,
    `disponibilidad` TINYINT      NOT NULL DEFAULT 0,
    `peticionAyuda`  varchar(255) NULL,
    PRIMARY KEY (`usuario`)
);