//
//  MainScreenView.swift
//  {{ cookiecutter.project_name }}
//
//  Created by {{ cookiecutter.author_name }}.
//

import SwiftUI

struct MainScreenView: View {
    @State private var viewModel: MainScreenViewModel
    private let presenter: MainScreenPresenter

    init(
        viewModel: MainScreenViewModel,
        presenter: MainScreenPresenter
    ) {
        _viewModel = State(wrappedValue: viewModel)
        self.presenter = presenter
    }

    var body: some View {
        VStack(spacing: 20) {
            Image(systemName: "car.fill")
                .font(.system(size: 80))
                .foregroundColor(.blue)

            Text(viewModel.title)
                .font(.largeTitle)
                .fontWeight(.bold)

            Text("Your car companion")
                .font(.subheadline)
                .foregroundColor(.secondary)
        }
        .onAppear {
            presenter.onAppear()
        }
    }
}
