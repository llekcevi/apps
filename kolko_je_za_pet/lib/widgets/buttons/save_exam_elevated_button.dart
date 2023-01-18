import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:kolko_je_za_pet/model.dart';
import 'package:kolko_je_za_pet/provider.dart';
import 'package:kolko_je_za_pet/hive_functions.dart';
import 'package:kolko_je_za_pet/screens/home_page.dart';

//ne treba consumer widget
class SaveExamElevatedButton extends StatelessWidget {
  const SaveExamElevatedButton({
    Key? key,
    required this.exam,
    required this.nazivController,
    required this.razredController,
    required this.bodoviController,
  }) : super(key: key);

  final Exam exam;
  final TextEditingController nazivController;
  final TextEditingController razredController;
  final TextEditingController bodoviController;

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
        onPressed: () {
          exam.naziv = nazivController.text;
          exam.razred = int.parse(razredController.text);
          addExamToBox(exam);
          clearTextEditingProviders(
              nazivController, razredController, bodoviController);
          Navigator.push(context,
              MaterialPageRoute(builder: ((context) => const HomePage())));
        },
        child: const Text("Završi"));
  }
}
