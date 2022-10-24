BEGIN;
--
-- Create model Bus
--
CREATE TABLE "dailycheck_bus" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "bus_number" varchar(255) NOT NULL, "capacity" integer NOT NULL, "plate" varchar(11) NOT NULL);
--
-- Create model City
--
CREATE TABLE "dailycheck_city" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "post_code" varchar(255) NOT NULL);
--
-- Create model District
--
CREATE TABLE "dailycheck_district" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "city_id" bigint NOT NULL REFERENCES "dailycheck_city" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Grade
--
CREATE TABLE "dailycheck_grade" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "level" varchar(255) NOT NULL, "branch" varchar(255) NOT NULL);
--
-- Create model Person
--
CREATE TABLE "dailycheck_person" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "username" varchar(255) NOT NULL, "password" varchar(255) NOT NULL, "first_name" varchar(255) NOT NULL, "last_name" varchar(255) NOT NULL, "role" varchar(1) NOT NULL);
--
-- Create model School
--
CREATE TABLE "dailycheck_school" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "code" integer NOT NULL, "address_detail" varchar(512) NULL, "is_active" bool NOT NULL, "city_id" bigint NULL REFERENCES "dailycheck_city" ("id") DEFERRABLE INITIALLY DEFERRED, "district_id" bigint NULL REFERENCES "dailycheck_district" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Village
--
CREATE TABLE "dailycheck_village" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "school_id" bigint NOT NULL REFERENCES "dailycheck_school" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Student
--
CREATE TABLE "dailycheck_student" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(255) NOT NULL, "last_name" varchar(255) NOT NULL, "bus_id" bigint NOT NULL REFERENCES "dailycheck_bus" ("id") DEFERRABLE INITIALLY DEFERRED, "grade_id" bigint NOT NULL REFERENCES "dailycheck_grade" ("id") DEFERRABLE INITIALLY DEFERRED, "school_id" bigint NOT NULL REFERENCES "dailycheck_school" ("id") DEFERRABLE INITIALLY DEFERRED, "village_id" bigint NOT NULL REFERENCES "dailycheck_village" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Signature
--
CREATE TABLE "dailycheck_signature" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "check_date" date NOT NULL, "direction" varchar(7) NOT NULL, "created_at" datetime NOT NULL, "signed_at" datetime NOT NULL, "is_signed" bool NOT NULL, "bus_id" bigint NOT NULL REFERENCES "dailycheck_bus" ("id") DEFERRABLE INITIALLY DEFERRED, "school_id" bigint NOT NULL REFERENCES "dailycheck_school" ("id") DEFERRABLE INITIALLY DEFERRED, "teacher_id" bigint NOT NULL REFERENCES "dailycheck_person" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field school to person
--
CREATE TABLE "new__dailycheck_person" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "username" varchar(255) NOT NULL, "password" varchar(255) NOT NULL, "first_name" varchar(255) NOT NULL, "last_name" varchar(255) NOT NULL, "role" varchar(1) NOT NULL, "school_id" bigint NOT NULL REFERENCES "dailycheck_school" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__dailycheck_person" ("id", "username", "password", "first_name", "last_name", "role", "school_id") SELECT "id", "username", "password", "first_name", "last_name", "role", NULL FROM "dailycheck_person";
DROP TABLE "dailycheck_person";
ALTER TABLE "new__dailycheck_person" RENAME TO "dailycheck_person";
CREATE INDEX "dailycheck_district_city_id_a05a03c3" ON "dailycheck_district" ("city_id");
CREATE INDEX "dailycheck_school_city_id_25fb60f6" ON "dailycheck_school" ("city_id");
CREATE INDEX "dailycheck_school_district_id_ffb64a98" ON "dailycheck_school" ("district_id");
CREATE INDEX "dailycheck_village_school_id_6227b07f" ON "dailycheck_village" ("school_id");
CREATE INDEX "dailycheck_student_bus_id_5dc76178" ON "dailycheck_student" ("bus_id");
CREATE INDEX "dailycheck_student_grade_id_528e35a5" ON "dailycheck_student" ("grade_id");
CREATE INDEX "dailycheck_student_school_id_ca3115a6" ON "dailycheck_student" ("school_id");
CREATE INDEX "dailycheck_student_village_id_f346f07a" ON "dailycheck_student" ("village_id");
CREATE INDEX "dailycheck_signature_bus_id_0e7e6b66" ON "dailycheck_signature" ("bus_id");
CREATE INDEX "dailycheck_signature_school_id_eb490593" ON "dailycheck_signature" ("school_id");
CREATE INDEX "dailycheck_signature_teacher_id_aab782a9" ON "dailycheck_signature" ("teacher_id");
CREATE INDEX "dailycheck_person_school_id_146509c8" ON "dailycheck_person" ("school_id");
--
-- Add field school to grade
--
CREATE TABLE "new__dailycheck_grade" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "level" varchar(255) NOT NULL, "branch" varchar(255) NOT NULL, "school_id" bigint NOT NULL REFERENCES "dailycheck_school" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__dailycheck_grade" ("id", "level", "branch", "school_id") SELECT "id", "level", "branch", NULL FROM "dailycheck_grade";
DROP TABLE "dailycheck_grade";
ALTER TABLE "new__dailycheck_grade" RENAME TO "dailycheck_grade";
CREATE INDEX "dailycheck_grade_school_id_1fca0d7b" ON "dailycheck_grade" ("school_id");
--
-- Create model Driver
--
CREATE TABLE "dailycheck_driver" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(255) NOT NULL, "last_name" varchar(255) NOT NULL, "school_id" bigint NOT NULL REFERENCES "dailycheck_school" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field driver to bus
--
ALTER TABLE "dailycheck_bus" ADD COLUMN "driver_id" bigint NULL REFERENCES "dailycheck_driver" ("id") DEFERRABLE INITIALLY DEFERRED;
--
-- Add field school to bus
--
CREATE TABLE "new__dailycheck_bus" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "bus_number" varchar(255) NOT NULL, "capacity" integer NOT NULL, "plate" varchar(11) NOT NULL, "driver_id" bigint NULL REFERENCES "dailycheck_driver" ("id") DEFERRABLE INITIALLY DEFERRED, "school_id" bigint NOT NULL REFERENCES "dailycheck_school" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__dailycheck_bus" ("id", "bus_number", "capacity", "plate", "driver_id", "school_id") SELECT "id", "bus_number", "capacity", "plate", "driver_id", NULL FROM "dailycheck_bus";
DROP TABLE "dailycheck_bus";
ALTER TABLE "new__dailycheck_bus" RENAME TO "dailycheck_bus";
CREATE INDEX "dailycheck_driver_school_id_1095dc46" ON "dailycheck_driver" ("school_id");
CREATE INDEX "dailycheck_bus_driver_id_4fcc4076" ON "dailycheck_bus" ("driver_id");
CREATE INDEX "dailycheck_bus_school_id_a57ce87b" ON "dailycheck_bus" ("school_id");
--
-- Add field village to bus
--
CREATE TABLE "new__dailycheck_bus" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "bus_number" varchar(255) NOT NULL, "capacity" integer NOT NULL, "plate" varchar(11) NOT NULL, "driver_id" bigint NULL REFERENCES "dailycheck_driver" ("id") DEFERRABLE INITIALLY DEFERRED, "school_id" bigint NOT NULL REFERENCES "dailycheck_school" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "dailycheck_bus_village" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "bus_id" bigint NOT NULL REFERENCES "dailycheck_bus" ("id") DEFERRABLE INITIALLY DEFERRED, "village_id" bigint NOT NULL REFERENCES "dailycheck_village" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__dailycheck_bus" ("id", "bus_number", "capacity", "plate", "driver_id", "school_id") SELECT "id", "bus_number", "capacity", "plate", "driver_id", "school_id" FROM "dailycheck_bus";
DROP TABLE "dailycheck_bus";
ALTER TABLE "new__dailycheck_bus" RENAME TO "dailycheck_bus";
CREATE INDEX "dailycheck_bus_driver_id_4fcc4076" ON "dailycheck_bus" ("driver_id");
CREATE INDEX "dailycheck_bus_school_id_a57ce87b" ON "dailycheck_bus" ("school_id");
CREATE UNIQUE INDEX "dailycheck_bus_village_bus_id_village_id_ad226826_uniq" ON "dailycheck_bus_village" ("bus_id", "village_id");
CREATE INDEX "dailycheck_bus_village_bus_id_3f6d37d6" ON "dailycheck_bus_village" ("bus_id");
CREATE INDEX "dailycheck_bus_village_village_id_afb149cf" ON "dailycheck_bus_village" ("village_id");
--
-- Create model Attendance
--
CREATE TABLE "dailycheck_attendance" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "signature_id" bigint NOT NULL REFERENCES "dailycheck_signature" ("id") DEFERRABLE INITIALLY DEFERRED, "student_id" bigint NOT NULL REFERENCES "dailycheck_student" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create constraint unique_signature_with_school_bus_date_and_direction on model signature
--
CREATE TABLE "new__dailycheck_signature" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "check_date" date NOT NULL, "direction" varchar(7) NOT NULL, "created_at" datetime NOT NULL, "signed_at" datetime NOT NULL, "is_signed" bool NOT NULL, "bus_id" bigint NOT NULL REFERENCES "dailycheck_bus" ("id") DEFERRABLE INITIALLY DEFERRED, "school_id" bigint NOT NULL REFERENCES "dailycheck_school" ("id") DEFERRABLE INITIALLY DEFERRED, "teacher_id" bigint NOT NULL REFERENCES "dailycheck_person" ("id") DEFERRABLE INITIALLY DEFERRED, CONSTRAINT "unique_signature_with_school_bus_date_and_direction" UNIQUE ("school_id", "bus_id", "check_date", "direction"));
INSERT INTO "new__dailycheck_signature" ("id", "check_date", "direction", "created_at", "signed_at", "is_signed", "bus_id", "school_id", "teacher_id") SELECT "id", "check_date", "direction", "created_at", "signed_at", "is_signed", "bus_id", "school_id", "teacher_id" FROM "dailycheck_signature";
DROP TABLE "dailycheck_signature";
ALTER TABLE "new__dailycheck_signature" RENAME TO "dailycheck_signature";
CREATE INDEX "dailycheck_attendance_signature_id_759bb0e1" ON "dailycheck_attendance" ("signature_id");
CREATE INDEX "dailycheck_attendance_student_id_6bf9f99b" ON "dailycheck_attendance" ("student_id");
CREATE INDEX "dailycheck_signature_bus_id_0e7e6b66" ON "dailycheck_signature" ("bus_id");
CREATE INDEX "dailycheck_signature_school_id_eb490593" ON "dailycheck_signature" ("school_id");
CREATE INDEX "dailycheck_signature_teacher_id_aab782a9" ON "dailycheck_signature" ("teacher_id");
--
-- Create constraint unique_attendance_with_student_and_signature on model attendance
--
CREATE TABLE "new__dailycheck_attendance" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "signature_id" bigint NOT NULL REFERENCES "dailycheck_signature" ("id") DEFERRABLE INITIALLY DEFERRED, "student_id" bigint NOT NULL REFERENCES "dailycheck_student" ("id") DEFERRABLE INITIALLY DEFERRED, CONSTRAINT "unique_attendance_with_student_and_signature" UNIQUE ("student_id", "signature_id"));
INSERT INTO "new__dailycheck_attendance" ("id", "signature_id", "student_id") SELECT "id", "signature_id", "student_id" FROM "dailycheck_attendance";
DROP TABLE "dailycheck_attendance";
ALTER TABLE "new__dailycheck_attendance" RENAME TO "dailycheck_attendance";
CREATE INDEX "dailycheck_attendance_signature_id_759bb0e1" ON "dailycheck_attendance" ("signature_id");
CREATE INDEX "dailycheck_attendance_student_id_6bf9f99b" ON "dailycheck_attendance" ("student_id");
COMMIT;
