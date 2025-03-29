use druid::{AppLauncher, WindowDesc, PlatformError, Widget};
use druid::widget::Label;

fn build_ui() -> impl Widget<()> {
    Label::new("Hello, Druid!")
}

fn main() -> Result<(), PlatformError> {
    let main_window = WindowDesc::new(build_ui()) 
        .title("Druid Example");

    AppLauncher::with_window(main_window)
        .launch(())
}
